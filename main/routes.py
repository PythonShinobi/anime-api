
import random
from flask import Blueprint, jsonify, render_template, request

from main import db
from main.models import Anime

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/random')
def get_random_anime():
    result = db.session.execute(db.select(Anime))
    all_anime = result.scalars().all()
    random_anime = random.choice(all_anime)
    return jsonify(anime=random_anime.to_dict())

@bp.route('/all')
def get_all_anime():
    result = db.session.execute(db.select(Anime).order_by(Anime.Name))
    all_anime = result.scalars().all()
    return jsonify(anime=[anime.to_dict() for anime in all_anime])

@bp.route('/search')
def get_anime_by_genre():
    genre = request.args.get('tag')
    result = db.session.execute(db.select(Anime).where(Anime.Tags.contains(genre)))
    all_anime = result.scalars().all()
    if all_anime:
        return jsonify(anime=[anime.to_dict() for anime in all_anime])
    else:
        return jsonify(message=f"No anime found for the specified tag: {genre}"), 404
    
@bp.route('/search-name')
def get_anime_by_name():
    name = request.args.get('name')
    if name is None:
        return jsonify(message="Name parameter is required"), 400
    
    result = db.session.query(Anime).filter(Anime.Name == name).all()
    if result:
        return jsonify(anime=[anime.to_dict() for anime in result])
    else:
        return jsonify(message=f"No anime found with the name: {name}"), 404
    
@bp.route('/add', methods=['POST'])
def add_new_anime():
    rank = request.form.get('rank')
    if rank is not None:  # Check if the rank is provided
        rank = int(rank)  # Convert to int if provided
    new_anime = Anime(
        Rank=request.form.get('rank'),
        Name=request.form.get('name'),
        Japanese_name=request.form.get('japanese_name'),
        Type=request.form.get('type'),
        Episodes=request.form.get('episodes'),
        Studio=request.form.get('studio'),
        Release_season=request.form.get('release_season'),
        Tags=request.form.get('tags'),
        Rating=request.form.get('rating'),
        Release_year=request.form.get('release_year'),
        End_year=request.form.get('end_year'),
        Description=request.form.get('description'),
        Content_warning=request.form.get('content_warning'),
        Related_mange=request.form.get('related_mange'),
        Related_anime=request.form.get('related_anime'),
        Voice_actors=request.form.get('voice_actors'),
        Staff=request.form.get('staff'),
    )
    db.session.add(new_anime)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new anime.'})

@bp.route('/update-name/<int:anime_id>', methods=['PATCH'])
def Update_name(anime_id):
    new_name = request.args.get('name')
    anime_model = db.get_or_404(Anime, anime_id)
    if anime_model:
        anime_model.Name = new_name
        db.session.commit()
        return jsonify(response={'success': 'Successfully updated the name.'}), 200
    else:
        return jsonify(error={'Not Found': 'Sorry anime with that id was not found in the database.'}), 404
    
@bp.route('/delete-anime/<int:anime_id>', methods=['DELETE'])
def delete_anime(anime_id):
    api_key = request.args.get('api-key')
    if api_key == 'TopSecretApiKey':
        anime_model = db.get_or_404(Anime, anime_id)
        if anime_id:
            db.session.delete(anime_model)
            db.session.commit()
            return jsonify(response={'success': 'Successfully deleted the anime from the database.'}), 200
        else:
            return jsonify(error={'Not Found': 'Sorry anime with id was not found in the database.'}), 404
    else:
        return jsonify(error={'Forbidden': 'Sorry, that\'s not allowed. Make sure you have the correct api_key'}),403